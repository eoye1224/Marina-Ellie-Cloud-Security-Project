### Ellie Oyebode and Marina Frayre  
### Adam Goldstein  
### CS 55 - Security and Privacy  
### 14 Aug 2024 - With Extension  

# Project Milestone 2 - System Design

## 1. Load Balancer

**Implementation:**  
Service: AWS Elastic Load Balancing (ELB)

**Setup:**  
- Create a new load balancer  
- Choose an Application Load Balancer for HTTP/HTTPS traffic  
- Register EC2 instances (web servers) with the load balancer.

**Configuration:**  
- Ensure the load balancer only directs traffic to healthy instances  
- Configure security groups to allow traffic from the load balancer to EC2 instances.

## 2. Web Server

**Implementation:**  
Service: Launch an EC2 instance with Apache

**Setup:**  
- Amazon Linux 2  
- Get static website files (HTML, CSS, JavaScript) onto `/var/www/html/`

**Configuration:**  
- Configure the security group to allow inbound traffic on port 80 (HTTP) or 443 (HTTPS).  
- Set up a basic firewall to restrict unnecessary ports.

## 3. Application Server

**Implementation:**  
Service: EC2 Instance with Backend Framework

**Setup:**  
- Amazon Linux 2  
- Implement matchmaking algorithms

**Configuration:**  
- Set up the application to listen on a specific port  
- Configure the security group to allow traffic only from the web server’s IP or security group.  
- Ensure the backend can access the database server securely.

## 4. Database Server

**Implementation:**  
Service: EC2 Instance with MySQL

**Setup (EC2-based):**  
- Install MySQL

**Setup (RDS-based):**  
- Create a new RDS instance with MySQL  
- Configure database parameters and security.

**Configuration:**  
- Configure the security group to allow traffic only from the application server.

## 5. Monitoring Instance

**Implementation:**  
Service: Use Amazon CloudWatch

**Setup:**  
- Configure CloudWatch to monitor EC2 instances.  
- Set up CloudWatch Alarms  
- Enable CloudWatch Logs to capture system logs and application logs.

**Configuration:**  
- Define metrics and thresholds for monitoring  
- Set up notifications for any triggered alarms.
