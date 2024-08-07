import React from "react";
import {Button, Navigation, Cell, Badge, Avatar, Info, Section, List, Card} from "@telegram-apps/telegram-ui";

import "./index.css"
import {useNavigate} from "react-router-dom";
import {instruction, game_menu} from "../../menu_routes.ts";
import {CardCell} from "@telegram-apps/telegram-ui/dist/components/Blocks/Card/components/CardCell/CardCell";
import { CardChip } from "@telegram-apps/telegram-ui/dist/components/Blocks/Card/components/CardChip/CardChip";


export const PlayerTypes = () => {

    return (
        <div>
            <a href="/" className="BackButton">Назад</a>
            <header><i>ТИПЫ ИГРОКОВ</i></header>
            <List>
                <Section>
                    <Card>
                        <React.Fragment key=".0">
                            <CardChip readOnly>
                                #1
                            </CardChip>
                            <img
                                alt="Dog"
                                src="https://i.imgur.com/892vhef.jpeg"
                                style={{
                                    display: 'block',
                                    height: 308,
                                    objectFit: 'cover',
                                    width: 254
                                }}
                            />
                            <CardCell
                                readOnly
                                subtitle="Ищут ящеров"
                            >
                                Русы
                            </CardCell>
                        </React.Fragment>
                    </Card>
                </Section>
                <Section>
                    <Card>
                        <React.Fragment key=".0">
                            <CardChip readOnly>
                                #2
                            </CardChip>
                            <img
                                alt="Dog"
                                src="https://i.imgur.com/892vhef.jpeg"
                                style={{
                                    display: 'block',
                                    height: 308,
                                    objectFit: 'cover',
                                    width: 254
                                }}
                            />
                            <CardCell
                                readOnly
                                subtitle="Выполняют задания"
                            >
                                Ящеры
                            </CardCell>
                        </React.Fragment>
                    </Card>
                </Section>
            </List>
        </div>
    )
}