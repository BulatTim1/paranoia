import '@telegram-apps/telegram-ui/dist/styles.css';

import {AppRoot} from '@telegram-apps/telegram-ui';
import {MainMenu} from "./components/MenuList";
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