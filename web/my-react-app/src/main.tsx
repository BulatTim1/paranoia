import * as React from "react";
import { createRoot } from "react-dom/client";
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import "./index.css"
import {AppRoot} from "@telegram-apps/telegram-ui";
import {Layout} from "./layouts/layout.tsx";
import '@telegram-apps/telegram-ui/dist/styles.css';
import {Home} from "./pages/home.tsx";
import {Players} from "./pages/playertypes.tsx"
import {Rules} from "./components/Rules";


const router = createBrowserRouter([
    {
        path: "/",
        element: <Home />
    },
    {
        path: "PlayerTypes",
        element: <Players />,
    },
    {
        path: "rules",
        element: <Rules />,
    }
]);

createRoot(document.getElementById("root")).render(
    <AppRoot>
        <Layout>
            <RouterProvider router={router} />
        </Layout>
    </AppRoot>
);
