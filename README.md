# My Vite Vue Ant Design App

This project is a front-end application built using Vite, Vue 3, TypeScript, and Ant Design Vue. It serves as a template for creating modern web applications with a focus on performance and developer experience.

## Project Structure

```
my-vite-vue-antd-app
├── index.html          # Main HTML file
├── package.json        # NPM configuration file
├── tsconfig.json       # TypeScript configuration file
├── tsconfig.node.json  # Node.js specific TypeScript configuration
├── vite.config.ts      # Vite configuration file
├── README.md           # Project documentation
├── public              # Public assets
│   └── .gitkeep        # Keeps the public directory in Git
└── src                 # Source code
    ├── App.vue         # Root Vue component
    ├── main.ts         # Entry point of the Vue application
    ├── env.d.ts        # Type declarations for environment variables
    ├── assets          # Asset files
    │   └── styles
    │       └── main.css # Main CSS styles
    ├── components      # Vue components
    │   └── HelloWorld.vue # Sample component
    ├── pages           # Page components
    │   └── Home.vue    # Home page component
    ├── router          # Vue Router setup
    │   └── index.ts    # Route definitions
    ├── store           # Vuex store setup
    │   └── index.ts    # Store instance
    └── plugins         # Plugin configurations
        └── antd.ts     # Ant Design Vue setup
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd my-vite-vue-antd-app
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   Navigate to `http://localhost:3000` to see your application in action.

## Usage Guidelines

- Modify the `src/pages/Home.vue` file to change the content of the Home page.
- Add new components in the `src/components` directory and import them into your pages as needed.
- Use the Vue Router defined in `src/router/index.ts` to create new routes for your application.
- Manage application state using Vuex in `src/store/index.ts`.
- Customize styles in `src/assets/styles/main.css`.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.