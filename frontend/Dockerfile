FROM node:14

WORKDIR /app

COPY package*.json ./
RUN npm install
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN npm run build

CMD ["npm", "start"]