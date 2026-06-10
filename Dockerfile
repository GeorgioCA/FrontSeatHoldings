# Front Seat Holdings — Static Site
FROM nginx:1.27-alpine

# Custom config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Site files
COPY img/ /usr/share/nginx/html/img/
COPY brand/ /usr/share/nginx/html/brand/
COPY index.html /usr/share/nginx/html/
COPY about.html /usr/share/nginx/html/
COPY careers.html /usr/share/nginx/html/
COPY contact.html /usr/share/nginx/html/
COPY swetrix.js /usr/share/nginx/html/
COPY css/ /usr/share/nginx/html/css/
COPY fr/ /usr/share/nginx/html/fr/

# Health check
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -qO- http://localhost:80/health || exit 1

EXPOSE 80
