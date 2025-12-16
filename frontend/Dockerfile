FROM node:18-alpine

WORKDIR /app

# Accept build-time variable
ARG VITE_API_BASE_URL
ENV VITE_API_BASE_URL=$VITE_API_BASE_URL

COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN npm run build

RUN npm install -g serve
CMD ["serve", "-s", "dist", "-l", "3000"]
