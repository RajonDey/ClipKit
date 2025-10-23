# Deployment Guide

## Production Deployment Options

### Option 1: Railway (Recommended for MVP)

#### Backend Deployment

1. **Create Railway account** and connect GitHub repository
2. **Add PostgreSQL** service from Railway marketplace
3. **Deploy backend:**
   ```bash
   # Set environment variables in Railway dashboard
   DATABASE_URL=<railway-postgres-url>
   SECRET_KEY=<your-secret-key>
   OPENAI_API_KEY=<your-openai-key>
   STRIPE_SECRET_KEY=<your-stripe-key>
   ```

#### Frontend Deployment

1. **Deploy to Vercel:**
   ```bash
   # Connect GitHub repository to Vercel
   # Set environment variables
   NEXT_PUBLIC_API_URL=<your-backend-url>
   NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=<your-stripe-key>
   ```

### Option 2: Docker Deployment

#### Using Docker Compose

```bash
# Production docker-compose
docker-compose -f docker-compose.prod.yml up -d
```

#### Manual Docker Deployment

```bash
# Build images
docker build -t clipkit-backend ./backend
docker build -t clipkit-frontend ./frontend

# Run containers
docker run -d -p 8000:8000 --env-file backend/.env clipkit-backend
docker run -d -p 3000:3000 --env-file frontend/.env.local clipkit-frontend
```

### Option 3: Cloud Providers

#### AWS

- **Backend**: ECS or EC2 with RDS
- **Frontend**: S3 + CloudFront
- **Database**: RDS PostgreSQL

#### Google Cloud

- **Backend**: Cloud Run
- **Frontend**: Firebase Hosting
- **Database**: Cloud SQL

#### Azure

- **Backend**: App Service
- **Frontend**: Static Web Apps
- **Database**: Azure Database for PostgreSQL

## Environment Configuration

### Backend Environment Variables

```bash
# Required
DATABASE_URL=postgresql://user:pass@host:port/db
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-key
STRIPE_SECRET_KEY=your-stripe-key

# Optional
REDIS_URL=redis://host:port
SENTRY_DSN=your-sentry-dsn
SMTP_HOST=smtp.gmail.com
SMTP_USER=your-email
SMTP_PASSWORD=your-password
```

### Frontend Environment Variables

```bash
# Required
NEXT_PUBLIC_API_URL=https://your-backend.com
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...

# Optional
NEXT_PUBLIC_GA_ID=your-ga-id
NEXT_PUBLIC_MIXPANEL_TOKEN=your-mixpanel-token
```

## Database Setup

### PostgreSQL Setup

1. **Create database:**

   ```sql
   CREATE DATABASE clipkit;
   CREATE USER clipkit_user WITH PASSWORD 'secure_password';
   GRANT ALL PRIVILEGES ON DATABASE clipkit TO clipkit_user;
   ```

2. **Run migrations:**
   ```bash
   cd backend
   alembic upgrade head
   ```

### Redis Setup (Optional)

```bash
# Install Redis
sudo apt-get install redis-server

# Configure Redis
sudo nano /etc/redis/redis.conf

# Start Redis
sudo systemctl start redis
sudo systemctl enable redis
```

## SSL Configuration

### Using Let's Encrypt

```bash
# Install Certbot
sudo apt-get install certbot

# Get SSL certificate
sudo certbot certonly --standalone -d yourdomain.com

# Configure Nginx
sudo nano /etc/nginx/sites-available/clipkit
```

### Using Cloudflare

1. Add domain to Cloudflare
2. Update nameservers
3. Enable SSL/TLS encryption mode: Full
4. Configure DNS records

## Monitoring Setup

### Application Monitoring

```bash
# Install Sentry CLI
npm install -g @sentry/cli

# Initialize Sentry
sentry-cli init
```

### Database Monitoring

```bash
# Install pgAdmin or use cloud provider dashboard
# Monitor slow queries and performance
```

### Log Management

```bash
# Configure log rotation
sudo nano /etc/logrotate.d/clipkit

# Set up log aggregation (optional)
# ELK Stack or similar
```

## Backup Strategy

### Database Backups

```bash
# Automated backup script
#!/bin/bash
pg_dump $DATABASE_URL > backup_$(date +%Y%m%d_%H%M%S).sql

# Upload to cloud storage
aws s3 cp backup_*.sql s3://your-backup-bucket/
```

### File Backups

```bash
# Backup uploaded files
rsync -av /var/www/clipkit/uploads/ /backup/uploads/
```

## Security Checklist

- [ ] HTTPS enabled
- [ ] Environment variables secured
- [ ] Database access restricted
- [ ] Firewall configured
- [ ] Regular security updates
- [ ] Backup strategy implemented
- [ ] Monitoring and alerting set up
- [ ] Rate limiting configured
- [ ] CORS properly configured
- [ ] Input validation implemented

## Performance Optimization

### Backend

- Enable database connection pooling
- Implement caching with Redis
- Use CDN for static assets
- Optimize database queries

### Frontend

- Enable Next.js optimizations
- Use image optimization
- Implement code splitting
- Enable compression

## Troubleshooting

### Common Issues

1. **Database connection errors**: Check DATABASE_URL and network connectivity
2. **CORS errors**: Verify CORS configuration in backend
3. **Environment variables**: Ensure all required variables are set
4. **SSL issues**: Check certificate validity and configuration

### Debug Commands

```bash
# Check backend logs
docker logs clipkit-backend

# Check database connectivity
psql $DATABASE_URL -c "SELECT 1;"

# Test API endpoints
curl -X GET https://your-backend.com/health
```
