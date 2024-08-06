import React from "react";
import {Search} from "../components/Search/search.tsx";
import {MainMenu} from "../components/ToDoList";
import '@telegram-apps/telegram-ui/dist/styles.css';

export const Home = () => {
    return (
        <div>
            <MainMenu/>
        </div>
    )
}
