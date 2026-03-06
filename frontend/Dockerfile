# Use Node.js for building and development
FROM node:20-slim

# Set working directory
WORKDIR /app

# Copy dependency manifests
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy application source code
COPY . .

# Expose Vite dev server port
EXPOSE 5173

# Bind the development server to all interfaces (required for Docker)
# This uses the --host flag to ensure accessibility outside the container
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
