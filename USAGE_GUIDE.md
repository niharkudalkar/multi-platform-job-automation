# Multi-Platform Job Automation - Usage Guide

## 📋 Overview

This is an advanced job automation script that searches for the latest job openings (posted within 24 hours) across multiple platforms:
- **Naukri.com** - India's largest job portal
- **LinkedIn Jobs** - Professional networking platform
- **Indeed** - Global job search engine

The script targets the following roles in **India (Remote)**:
- Product Manager
- Senior Product Manager
- Director
- Program Manager
- Automation Expert
- Project Manager

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/multi-platform-job-automation.git
cd multi-platform-job-automation

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Update `candidate_config.py` with your information:

```python
# Example
CANDIDATE = {
    'first_name': 'Your Name',
    'last_name': 'Your Surname',
    'email': 'your.email@example.com',
    'phone': '+91 XXXXXXXXXX',
    'linkedin': 'https://www.linkedin.com/in/yourprofile/',
}

SALARY = {
    'current_ctc': 2100000,  # in rupees
    'expected_ctc': 2800000,
    'notice_period': 'Serving Notice Period'
}

RESUME_PATH = 'your_resume.pdf'  # Path to your resume
```

### 3. Run the Script

```bash
# Basic execution
python job_automation.py
```

## 📊 Output Files

After execution, the script generates:

### `job_applications_results.json`

Contains:
- Total jobs found across all platforms
- Successfully applied jobs
- Jobs requiring manual application
- Direct company application links

Example output:
```json
{
  "timestamp": "2025-12-30T15:30:45.123456",
  "total_jobs_found": 47,
  "jobs_applied": 10,
  "jobs_failed": 37,
  "applied_jobs": [...],
  "manual_apply_links": [
    {
      "title": "Product Manager",
      "company": "Company Name",
      "platform": "LinkedIn",
      "apply_url": "https://...",
      "location": "Remote"
    }
  ]
}
```

## 🔧 Features

✅ **Multi-Platform Support**
- Search across Naukri.com, LinkedIn, and Indeed
- Aggregate results from all platforms

✅ **Smart Job Filtering**
- Targets 24-hour job postings only
- Filters for Remote work mode
- Focus on Product Manager, Director, and related roles

✅ **Auto-Apply Capability**
- Attempts automatic form filling and submission
- Uses Selenium for browser automation
- Uploads resume automatically

✅ **Manual Links Export**
- Provides direct company links when auto-apply fails
- Includes job title, company, and application URL
- Exported in JSON format for easy tracking

✅ **Comprehensive Logging**
- Detailed execution logs
- Error tracking and reporting
- Status updates for each application

## 📝 Configuration Options

### candidate_config.py

**CANDIDATE** - Personal information for form filling
**SALARY** - Current and expected CTC details
**COMPETENCIES** - List of your skills
**WORK_EXPERIENCE** - Job history
**CERTIFICATIONS** - Relevant certifications
**SCREENING_ANSWERS** - Common screening question answers

## 🎯 Supported Job Titles

- Product Manager
- Senior Product Manager
- Lead Product Manager
- Director
- Program Manager
- Automation Expert
- Automation Manager
- Project Manager
- Senior Project Manager

## 🌍 Location Targeting

- **Primary**: India (Remote)
- **Work Mode**: Work from Home (WFH)
- **Job Freshness**: Posted within last 24 hours

## 📌 Important Notes

1. **Resume Format**: Use PDF, DOC, or DOCX format
2. **Resume Size**: Keep under 5 MB
3. **Network**: Ensure stable internet connection
4. **Chrome Browser**: Must have Google Chrome installed
5. **Execution Time**: Script typically takes 15-30 minutes

## 🔐 Security & Privacy

- No credentials are stored
- Resume file is used locally only
- Application data is exported to JSON
- Update `.gitignore` if sharing credentials

## 🛠️ Troubleshooting

### Chrome WebDriver Issues
```bash
pip install --upgrade webdriver-manager
```

### Resume Not Uploading
- Verify file format (PDF recommended)
- Check file size (< 5 MB)
- Ensure correct file path in config

### Script Hangs
- Increase timeout values in job_automation.py
- Check internet connection
- Verify Chrome is not in use by another process

## 📈 Results Tracking

Monitor your applications using:

1. **JSON Output**: `job_applications_results.json`
2. **Platform Dashboards**:
   - Naukri.com: My Applications
   - LinkedIn: Application Tracking
   - Indeed: Application Status

3. **Email Notifications**: Check registered email for confirmations

## 🚀 Advanced Usage

### Custom Job Titles
Edit `job_titles` list in `job_automation.py` to target specific roles

### Multiple Runs
Schedule the script using:
- **Windows**: Task Scheduler
- **Linux/Mac**: cron jobs

### Data Analysis
Export `job_applications_results.json` to spreadsheet for tracking:
- Application dates
- Success rates per platform
- Company tracking

## 📞 Support

For issues or suggestions:
1. Check existing GitHub issues
2. Create a detailed issue report
3. Include execution logs
4. Provide configuration snippet (without sensitive data)

## ⚖️ Legal Disclaimer

This tool is for personal job automation only. Users are responsible for:
- Complying with website terms of service
- Providing accurate information
- Respecting application guidelines
- Following job portal policies

## 📄 License

MIT License - Feel free to use and modify for personal use

## 👨‍💻 Author

**Nihar Kudalkar**
- Email: Nihar.kudalkar@yahoo.com
- LinkedIn: https://www.linkedin.com/in/niharkudalkar/
- GitHub: https://github.com/niharkudalkar
