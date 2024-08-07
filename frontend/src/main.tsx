import {createRoot} from "react-dom/client";
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
import {Rules_page} from "./pages/rules.tsx";
import {Lizardtasks_page} from "./pages/lizard-tasks.tsx";
import {Task1} from "./components/result/task1.tsx";
import {Task2} from "./components/result/task2.tsx";
import {Task3} from "./components/result/task3.tsx";
import {Task4} from "./components/result/task4.tsx";
import {Task5} from "./components/result/task5.tsx";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <Home/>
    },
    {
        path: "PlayerTypes",
        element: <Players/>,
    },
    {
        path: "rules",
        element: <Rules_page />,
    },
    {
        path: "lizard-tasks",
        element: <Lizardtasks_page />,
    },
    {
        path: "task1",
        element: <Task1 />
    },
    {
        path: "task2",
        element: <Task2 />
    },
    {
        path: "task3",
        element: <Task3 />
    },
    {
        path: "task4",
        element: <Task4 />
    },
    {
        path: "task5",
        element: <Task5 />
    }
]);

// @ts-ignore
createRoot(document.getElementById("root")).render(
    <AppRoot>
        <Layout>
            <RouterProvider router={router}/>
        </Layout>
    </AppRoot>
);
