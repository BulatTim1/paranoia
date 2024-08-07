import {Cell, Image, List, Navigation, Section} from "@telegram-apps/telegram-ui";

import "./index.css"
import {useNavigate} from "react-router-dom";
import {game_menu} from "../../menu_routes.ts";


export const Task3 = () => {

    const navigate = useNavigate()

    const handleClick = () => {
        navigate("/task4");
    }


    return (
        <div>
            <a href="/" className="BackButton">Назад</a>
            <List>
                <header><i>Действие</i></header>
                <Section.Footer>
                    Сфотографироваться с 6 незнакомыми людьми
                </Section.Footer>
                <header><i>Игра</i></header>
                <Section>

                    <Cell onClick={() => handleClick()}
                          after={<Navigation className="arrow"/>}
                    >
                        "Видел"
                    </Cell>
                </Section>
                <Section>
                    <Cell onClick={() => handleClick()}
                          after={<Navigation className="arrow"/>}
                    >
                        "Не видел"
                    </Cell>
                </Section>

            </List>
        </div>
    )
}