import '@telegram-apps/telegram-ui/dist/styles.css';

import {AppRoot, Placeholder} from '@telegram-apps/telegram-ui';
import '@telegram-apps/telegram-ui/dist/styles.css';
import {Layout} from "./Layouts/layout.tsx";
import {MainMenu} from "./components/MenuList";
import React from "react";

const App = () => (
    <AppRoot>
        <MainMenu/>
    </AppRoot>

);

export default App;