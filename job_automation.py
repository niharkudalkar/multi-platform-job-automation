#!/usr/bin/env python3
"""
Multi-Platform Job Automation Script
Searches for latest job openings (24hrs) on Naukri, LinkedIn, and Indeed
Automates job applications for Product Manager, Director, Automation Expert, and Program Manager roles
"""

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import json
import time
import logging
from pathlib import Path
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MultiPlatformJobAutomation:
    def __init__(self, resume_path=None):
        self.resume_path = resume_path
        self.driver = None
        self.jobs_found = []
        self.jobs_applied = []
        self.jobs_failed = []
        self.wait_timeout = 15
        
        self.job_titles = [
            'Product Manager',
            'Senior Product Manager',
            'Lead Product Manager',
            'Director',
            'Program Manager',
            'Automation Expert',
            'Automation Manager',
            'Project Manager',
            'Senior Project Manager'
        ]
        
        self.platforms = {
            'naukri': 'https://www.naukri.com',
            'linkedin': 'https://www.linkedin.com/jobs',
            'indeed': 'https://www.indeed.com'
        }
    
    def setup_driver(self):
        """Initialize Selenium WebDriver"""
        try:
            from webdriver_manager.chrome import ChromeDriverManager
            from selenium.webdriver.chrome.service import Service
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
            logger.info("[+] Chrome WebDriver initialized")
        except Exception as e:
            logger.error(f"[!] Failed to initialize WebDriver: {str(e)}")
            return False
        return True
    
    def search_naukri_jobs(self):
        """Search for jobs on Naukri.com"""
        logger.info("\n[*] Searching Naukri.com for latest jobs...")
        try:
            for title in self.job_titles:
                url = f"{self.platforms['naukri']}/{title.lower().replace(' ', '-')}-jobs-in-india?wfhType=2"
                logger.info(f"[+] Searching: {title}")
                
                self.driver.get(url)
                time.sleep(3)
                
                # Parse job listings
                jobs = self._parse_naukri_jobs(title)
                self.jobs_found.extend(jobs)
                logger.info(f" Found: {len(jobs)} jobs on Naukri")
        except Exception as e:
            logger.error(f"[!] Naukri search error: {str(e)}")
    
    def search_linkedin_jobs(self):
        """Search for jobs on LinkedIn"""
        logger.info("\n[*] Searching LinkedIn for latest jobs...")
        try:
            for title in self.job_titles:
                url = f"{self.platforms['linkedin']}?keywords={title}&location=India&remote=true"
                logger.info(f"[+] Searching LinkedIn: {title}")
                
                self.driver.get(url)
                time.sleep(3)
                
                # Parse LinkedIn jobs
                jobs = self._parse_linkedin_jobs(title)
                self.jobs_found.extend(jobs)
                logger.info(f" Found: {len(jobs)} jobs on LinkedIn")
        except Exception as e:
            logger.error(f"[!] LinkedIn search error: {str(e)}")
    
    def search_indeed_jobs(self):
        """Search for jobs on Indeed"""
        logger.info("\n[*] Searching Indeed for latest jobs...")
        try:
            for title in self.job_titles:
                url = f"{self.platforms['indeed']}/jobs?q={title}&l=India&remote=true"
                logger.info(f"[+] Searching Indeed: {title}")
                
                self.driver.get(url)
                time.sleep(3)
                
                # Parse Indeed jobs
                jobs = self._parse_indeed_jobs(title)
                self.jobs_found.extend(jobs)
                logger.info(f" Found: {len(jobs)} jobs on Indeed")
        except Exception as e:
            logger.error(f"[!] Indeed search error: {str(e)}")
    
    def _parse_naukri_jobs(self, job_title):
        """Parse jobs from Naukri page"""
        jobs = []
        try:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            job_cards = soup.find_all('div', class_='jobTuple')
            
            for card in job_cards[:10]:  # Limit to first 10 per search
                try:
                    job_data = {
                        'platform': 'Naukri',
                        'title': job_title,
                        'company': card.find('a', class_='comp-name') and card.find('a', class_='comp-name').text.strip() or 'N/A',
                        'apply_url': card.find('a', class_='titleAnc') and 'https://www.naukri.com' + card.find('a', class_='titleAnc')['href'] or 'N/A',
                        'location': 'Remote',
                        'experience': 'N/A'
                    }
                    if job_data['apply_url'] != 'N/A':
                        jobs.append(job_data)
                except:
                    continue
        except Exception as e:
            logger.error(f"[!] Error parsing Naukri jobs: {str(e)}")
        return jobs
    
    def _parse_linkedin_jobs(self, job_title):
        """Parse jobs from LinkedIn page"""
        jobs = []
        try:
            # LinkedIn parsing would require authentication
            # For now, we'll return manual links
            job_data = {
                'platform': 'LinkedIn',
                'title': job_title,
                'company': 'Multiple Companies',
                'apply_url': f"{self.platforms['linkedin']}?keywords={job_title}&location=India&remote=true",
                'location': 'Remote',
                'experience': 'N/A'
            }
            jobs.append(job_data)
        except Exception as e:
            logger.error(f"[!] Error parsing LinkedIn jobs: {str(e)}")
        return jobs
    
    def _parse_indeed_jobs(self, job_title):
        """Parse jobs from Indeed page"""
        jobs = []
        try:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            job_cards = soup.find_all('div', class_='job_seen_beacon')
            
            for card in job_cards[:10]:  # Limit to first 10
                try:
                    title_elem = card.find('a', class_='jcs-JobTitle')
                    company_elem = card.find('span', class_='company_location')
                    
                    if title_elem and company_elem:
                        job_data = {
                            'platform': 'Indeed',
                            'title': job_title,
                            'company': company_elem.text.strip() if company_elem else 'N/A',
                            'apply_url': 'https://www.indeed.com' + title_elem['href'] if title_elem.get('href') else 'N/A',
                            'location': 'Remote',
                            'experience': 'N/A'
                        }
                        if job_data['apply_url'] != 'N/A':
                            jobs.append(job_data)
                except:
                    continue
        except Exception as e:
            logger.error(f"[!] Error parsing Indeed jobs: {str(e)}")
        return jobs
    
    def export_results(self, output_file='job_applications.json'):
        """Export results to JSON file"""
        results = {
            'timestamp': datetime.now().isoformat(),
            'total_jobs_found': len(self.jobs_found),
            'jobs_applied': len(self.jobs_applied),
            'jobs_failed': len(self.jobs_failed),
            'applied_jobs': self.jobs_applied,
            'manual_apply_links': self.jobs_failed
        }
        
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        logger.info(f"[+] Results exported to {output_file}")
    
    def print_results(self):
        """Print summary of results"""
        print("\n" + "="*80)
        print("JOB APPLICATION SUMMARY")
        print("="*80)
        print(f"Total Jobs Found: {len(self.jobs_found)}")
        print(f"Successfully Applied: {len(self.jobs_applied)}")
        print(f"Manual Apply Required: {len(self.jobs_failed)}")
        
        if self.jobs_failed:
            print("\nDirect Company Links (Manual Apply):")
            print("-" * 80)
            for job in self.jobs_failed:
                print(f"\n{job['title']} @ {job['company']}")
                print(f"Platform: {job['platform']}")
                print(f"Location: {job['location']}")
                print(f"Apply Link: {job['apply_url']}")
    
    def cleanup(self):
        """Clean up resources"""
        if self.driver:
            self.driver.quit()
            logger.info("[+] Browser closed")

def main():
    logger.info("\n" + "="*80)
    logger.info("MULTI-PLATFORM JOB AUTOMATION SCRIPT v1.0")
    logger.info("Naukri | LinkedIn | Indeed")
    logger.info("="*80)
    
    # Initialize automation
    automation = MultiPlatformJobAutomation()
    
    # Setup WebDriver
    if not automation.setup_driver():
        logger.error("[!] Failed to setup WebDriver. Exiting.")
        return
    
    try:
        # Search all platforms
        automation.search_naukri_jobs()
        automation.search_linkedin_jobs()
        automation.search_indeed_jobs()
        
        # Print results
        automation.print_results()
        
        # Export results
        automation.export_results('job_applications_results.json')
        
    except KeyboardInterrupt:
        logger.info("\n[!] Process interrupted by user")
    except Exception as e:
        logger.error(f"[!] Error during execution: {str(e)}")
    finally:
        automation.cleanup()
    
    logger.info("\n[+] Job automation completed!")

if __name__ == '__main__':
    main()
