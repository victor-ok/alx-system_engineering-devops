Issue Summary:

Duration: The outage spanned from April 15, 2024, starting at 3:45 PM UTC and lasting for about 2 hours until 5:45 PM UTC.

Impact: The web application's login and authentication service were impacted, causing users to face intermittent login failures and slow response times. Roughly 30% of users encountered difficulties accessing the platform during this period, resulting in a significant disruption.

Root Cause: A misconfiguration in the database connection pool settings caused a database connection issue, leading to the outage.

Timeline:

3:45 PM UTC: The issue was flagged by monitoring alerts, indicating a sudden surge in login failures and database connection errors.

3:50 PM UTC: Engineers initiated an investigation, initially suspecting a possible database server malfunction due to the increased errors.

4:15 PM UTC: Attention shifted towards scrutinizing the application server configurations, particularly focusing on the database connection pool settings.

4:45 PM UTC: The root cause was identified as misconfigured database connection pool settings, resulting in excessive open connections and connection timeouts.

5:00 PM UTC: The incident was escalated to the DevOps team to assist in resolving the misconfiguration.

5:30 PM UTC: Corrective measures were applied to adjust the database connection pool settings, optimizing pool size and timeout parameters.

5:45 PM UTC: With the adjustments made, normal service resumed, and the issue was resolved.

Root Cause and Resolution:

Root Cause Explanation: The misconfiguration of database connection pool settings caused an overflow of open connections, leading to connection timeouts and service disruptions.

Resolution: The issue was rectified by fine-tuning the database connection pool settings to optimize connection pool size and timeout parameters, ensuring efficient management of database connections.

Corrective and Preventative Measures:

Improvements/Fixes:

Deploy automated monitoring for database connection pool health and performance metrics.
Conduct routine reviews of database connection pool configurations to maintain optimal settings.
Establish a process for testing and validating changes to database connection pool settings before deployment.
Tasks to Address the Issue:

Adjust database connection pool settings to optimize pool size and timeout parameters.
Implement automated monitoring for database connection pool health and performance.
Perform a comprehensive review of application server configurations to identify and rectify any misconfigurations.
Enhance incident response protocols to include specific steps for troubleshooting database connection issues.
By implementing these corrective and preventative measures, our aim is to minimize the occurrence of similar outages in the future, ensuring improved stability and reliability of our web application services.