import {Cell, Image, List, Navigation, Section} from "@telegram-apps/telegram-ui";

import "./index.css"
import {useNavigate} from "react-router-dom";
import {game_menu, instruction} from "../../menu_routes.ts";


export const MainMenu = () => {

    const navigate = useNavigate()

    const handleClick = (path: string) => {
        navigate(path);
    }




    return (
        <List>
            <header><i>Правила игры</i></header>
            <Section>
                {instruction.map((el) => (
                    <Cell onClick={() => handleClick(el.path)}
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
                    <Cell onClick={() => handleClick(el.path)}
                          before={<Image size={48} src={el.image}></Image>}
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