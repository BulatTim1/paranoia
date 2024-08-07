import '@telegram-apps/telegram-ui/dist/styles.css';

import {AppRoot, Placeholder} from '@telegram-apps/telegram-ui';
import '@telegram-apps/telegram-ui/dist/styles.css';
import {Layout} from "./Layouts/layout.tsx";
import {MainMenu} from "./components/MenuList";
import React from "react";
import {retrieveLaunchParams} from "@telegram-apps/sdk";
import {SDKProvider} from "@telegram-apps/sdk-react";



const App = () => {
    const {initDataRaw} = retrieveLaunchParams();

    alert(initDataRaw);

    // fetch('https://example.com/api', {
    //     method: 'POST',
    //     headers: {
    //         Authorization: `tma ${initDataRaw}`
    //     },
    // });

    <SDKProvider>
        <AppRoot>
            <MainMenu/>
        </AppRoot>
    </SDKProvider>
};

export default App;