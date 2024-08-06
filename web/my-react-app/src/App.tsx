import '@telegram-apps/telegram-ui/dist/styles.css';

import {AppRoot, Placeholder} from '@telegram-apps/telegram-ui';
import {Layout} from "./Layouts/layout.tsx";
import {MainMenu} from "./components/ToDoList";
import React from "react";

const App = () => (
    <AppRoot>
        <MainMenu/>
    </AppRoot>

);

export default App;