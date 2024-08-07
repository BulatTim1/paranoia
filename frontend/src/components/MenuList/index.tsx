import React from "react";
import { Button, Navigation, Cell, Badge, Avatar, Info, Section, List } from "@telegram-apps/telegram-ui";
import { retrieveLaunchParams } from '@telegram-apps/sdk';
import { Button, Navigation, Cell, Badge, Avatar, Info, Section, List, Image } from "@telegram-apps/telegram-ui";

import "./index.css"
import { useNavigate } from "react-router-dom";
import { instruction, game_menu } from "../../menu_routes.ts";


export const MainMenu = () => {

    const navigate = useNavigate()

    const handleClick = (path: string) => {
        navigate(path);
    }

    const { initDataRaw } = retrieveLaunchParams();
    console.log(initDataRaw)
    // fetch('https://example.com/api', {
    //     method: 'POST',
    //     headers: {
    //         Authorization: `tma ${initDataRaw}`
    //     },
    // });


    return (
        <List>
            <header><i>Правила игры</i></header>
            <Section>
                {instruction.map((el) => (
                    <Cell
                        before={<Image size={48} src={el.image}></Image>}
                        after={<Navigation className="arrow" />}
                        subtitle={el.description}
                    >
                        {el.text}
                    </Cell>
                ))}
            </Section>
            <header><i>Игра</i></header>
            <Section>
                {game_menu.map((el) => (
                    <Cell
                        before={<Avatar size={48} />}
                        after={<Navigation className="arrow" />}
                        subtitle={el.description}
                    >
                        {el.text}
                    </Cell>
                ))}
            </Section>
        </List>
    )
}