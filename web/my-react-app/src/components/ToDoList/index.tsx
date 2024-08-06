import React from "react";
import {Button, Navigation, Cell, Badge, Avatar, Info} from "@telegram-apps/telegram-ui";

import "./index.css"
import {useNavigate} from "react-router-dom";
import {instruction, game_menu} from "../../menu_routes.ts";


export const MainMenu = () => {

    return (
        <div>
            <div className="upper"><i>Правила игры</i></div>
            {instruction.map((el) => (
                <div className="Items">
                    <div>
                        <div className="name">{el.text}</div>
                        <div className="description">{el.description}</div>
                    </div>
                    <div>
                        <Navigation></Navigation>

                    </div>
                </div>
            ))}
            <div className="upper"><i>Игра</i></div>
            {game_menu.map((el) => (
                <Cell
                    before={<Avatar size={48}/>}
                    subtitle={el.description}
                >
                    {el.text}
                </Cell>
            ))}


        </div>
    )
}