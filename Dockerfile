# Front Seat Holdings — Static Site
FROM nginx:1.27-alpine

# Custom config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Site files
COPY Founder-Georgio.png /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/
COPY about.html /usr/share/nginx/html/
COPY fr.html /usr/share/nginx/html/
COPY a-propos.html /usr/share/nginx/html/
COPY carrieres.html /usr/share/nginx/html/
COPY careers.html /usr/share/nginx/html/
COPY brand/ /usr/share/nginx/html/brand/

# Health check
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -qO- http://localhost:80/ || exit 1

EXPOSE 80
