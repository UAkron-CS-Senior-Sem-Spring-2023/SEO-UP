# Setup Node
FROM node:18 as base

WORKDIR /app

# Doing it in this order helps caching
COPY package* yarn.lock ./
RUN yarn install

COPY astro.config.mjs ./
COPY tsconfig.json ./
COPY public ./public/
COPY src ./src/

FROM base as dev
CMD ["yarn", "dev", "--host"]
