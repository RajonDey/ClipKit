# 🚀 ClipKit Production Maintenance Guide

## 📋 **Quick Reference**

### **Your Live URLs:**
- **Frontend**: `https://clip-kit.vercel.app`
- **Backend**: `https://clipkit.onrender.com`
- **Database**: PostgreSQL on Render

---

## 🔄 **Making Changes & Deploying**

### **Step 1: Make Changes Locally**
```bash
# 1. Make your code changes
# 2. Test locally
npm run dev          # Frontend
uvicorn app.main:app # Backend
```

### **Step 2: Commit & Push**
```bash
git add .
git commit -m "Your change description"
git push origin main
```

### **Step 3: Auto-Deploy**
- **Frontend (Vercel)**: Automatically deploys from GitHub
- **Backend (Render)**: Automatically deploys from GitHub

---

## 🛠 **Common Tasks**

### **Adding New Features**
1. **Frontend Changes**: Edit files in `clipkit-app/frontend/src/`
2. **Backend Changes**: Edit files in `clipkit-app/backend/app/`
3. **Database Changes**: Create migration in `clipkit-app/backend/alembic/versions/`

### **Database Migrations**
```bash
# Create new migration
cd clipkit-app/backend
alembic revision --autogenerate -m "Description of changes"

# Apply migration (happens automatically on Render)
alembic upgrade head
```

### **Environment Variables**
- **Frontend (Vercel)**: Dashboard → Settings → Environment Variables
- **Backend (Render)**: Dashboard → Environment Variables

---

## 🔍 **Monitoring & Debugging**

### **Check Logs**
- **Frontend**: Vercel Dashboard → Functions → View Logs
- **Backend**: Render Dashboard → Logs tab

### **Health Checks**
- **Backend Health**: `https://clipkit.onrender.com/health`
- **API Docs**: `https://clipkit.onrender.com/docs`

### **Common Issues**
1. **500 Errors**: Check Render logs
2. **CORS Issues**: Update `ALLOWED_ORIGINS` in Render
3. **Build Failures**: Check GitHub Actions or deployment logs

---

## 🚨 **Emergency Procedures**

### **Rollback Deployment**
1. **Vercel**: Dashboard → Deployments → Rollback
2. **Render**: Dashboard → Manual Deploy → Previous commit

### **Database Issues**
1. Check Render PostgreSQL logs
2. Run migrations manually if needed
3. Contact Render support for critical issues

---

## 📊 **Performance Monitoring**

### **Free Tier Limits**
- **Vercel**: 100GB bandwidth/month
- **Render**: 750 hours/month (Free tier sleeps after inactivity)
- **PostgreSQL**: 1GB storage

### **Upgrade When Needed**
- **Vercel Pro**: $20/month for more bandwidth
- **Render Starter**: $7/month for always-on backend
- **PostgreSQL**: Upgrade for more storage

---

## 🔐 **Security Checklist**

### **Regular Maintenance**
- [ ] Update dependencies monthly
- [ ] Check for security vulnerabilities
- [ ] Monitor logs for unusual activity
- [ ] Backup database regularly

### **Environment Variables**
- [ ] Keep `SECRET_KEY` secure
- [ ] Rotate keys periodically
- [ ] Never commit secrets to Git

---

## 📞 **Support Resources**

### **Platform Support**
- **Vercel**: [vercel.com/support](https://vercel.com/support)
- **Render**: [render.com/docs](https://render.com/docs)
- **PostgreSQL**: [postgresql.org/docs](https://postgresql.org/docs)

### **Your Application**
- **Frontend Code**: `clipkit-app/frontend/`
- **Backend Code**: `clipkit-app/backend/`
- **Database**: PostgreSQL on Render

---

## 🎯 **Quick Commands**

```bash
# Local Development
npm run dev                    # Start frontend
uvicorn app.main:app --reload  # Start backend

# Database
alembic upgrade head          # Apply migrations
alembic revision --autogenerate -m "message"  # Create migration

# Deployment
git add . && git commit -m "message" && git push  # Deploy everything
```

---

## ✅ **Deployment Checklist**

Before pushing to production:
- [ ] Test changes locally
- [ ] Check for TypeScript/ESLint errors
- [ ] Verify database migrations
- [ ] Test API endpoints
- [ ] Check environment variables
- [ ] Monitor deployment logs

---

**🎉 Your ClipKit is production-ready! Happy coding!**
