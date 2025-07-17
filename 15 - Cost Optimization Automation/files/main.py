import boto3
from datetime import datetime, timedelta

# AWS Clients
ce = boto3.client('ce')
ses = boto3.client('ses', region_name='ap-south-1') 

# Date range
end = datetime.today().date()
start = end - timedelta(days=7)

# 1. Get cost and usage data
def get_cost_data():
    return ce.get_cost_and_usage(
        TimePeriod={'Start': str(start), 'End': str(end)},
        Granularity='DAILY',
        Metrics=['UnblendedCost', 'UsageQuantity'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )

# 2. Analyze and find underutilized services
def analyze(data):
    report = []
    for day in data['ResultsByTime']:
        for item in day['Groups']:
            service = item['Keys'][0]
            cost = float(item['Metrics']['UnblendedCost']['Amount'])
            usage = float(item['Metrics']['UsageQuantity']['Amount'])

            if cost > 5 and usage < 1:
                report.append(f"{service} on {day['TimePeriod']['Start']}: Cost = ${cost:.2f}, Usage = {usage:.2f}")
    return report

# 3. Send report email
def send_email(report_lines):
    if not report_lines:
        print("No underutilized services found.")
        ses.send_email(
        Source="dineshkarasu137@gmail.com",
        Destination={"ToAddresses": ["dkarasu@evoketechnologies.com"]},
        Message={
            "Subject": {"Data": "AWS Cost Optimization Report"},
            "Body": {"Html": {"Data": "No underutilized services found."}}
            }
        )
        return

    body = "<h2>Underutilized AWS Services</h2><ul>"
    body += ''.join([f"<li>{line}</li>" for line in report_lines])
    body += "</ul>"

    ses.send_email(
        Source="dineshkarasu137@gmail.com",
        Destination={"ToAddresses": ["dkarasu@evoketechnologies.com"]},
        Message={
            "Subject": {"Data": "AWS Cost Optimization Report"},
            "Body": {"Html": {"Data": body}}
        }
    )
    print("Email sent!")

# 4. Run all
if __name__ == "__main__":
    cost_data = get_cost_data()
    underutilized_services = analyze(cost_data)
    send_email(underutilized_services)

    # Simulated underutilized service list
    fake_report = [
        "Amazon EC2 on 2025-06-23: Cost = $10.00, Usage = 0.30",
        "Amazon RDS on 2025-06-24: Cost = $6.00, Usage = 0.10"
    ]

    # Test the email function directly
    send_email(fake_report)
