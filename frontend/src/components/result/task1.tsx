import {Cell, List, Navigation, Section} from "@telegram-apps/telegram-ui";

import "./index.css"
import {useNavigate} from "react-router-dom";


export const Task1 = () => {

    const navigate = useNavigate()

    const handleClick = () => {
        navigate("/task2");
    }


    return (
        <div>
            <a href="/" className="BackButton">Назад</a>
            <List>
                <header><i>Действие</i></header>
                <Section.Footer>
                    Подойти и дать пять семерым людям в одном месте
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