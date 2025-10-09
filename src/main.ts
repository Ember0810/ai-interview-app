import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
// import store from './store';
import { setupAntd } from './plugins/antd';
import 'virtual:svg-icons-register'; 
import 'ant-design-vue/dist/antd.css'

const app = createApp(App);

setupAntd(app);
app.use(router);
// app.use(store);

app.mount('#app');