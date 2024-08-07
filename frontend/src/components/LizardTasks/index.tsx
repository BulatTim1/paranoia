import {List, Section} from "@telegram-apps/telegram-ui";

import "./index.css"

export const LizardTasks = () => {

    return (
        <div>
            <a href="/" className="BackButton">Назад</a>
            <List>
                <header><i>Task 1</i></header>
                <Section.Footer>
                    Ты должен подойти и дать пять семерым людям в одном месте
                </Section.Footer>
                <header><i>Task 2</i></header>
                <Section.Footer>
                    Угостить печеньем/снеками 5 человек
                </Section.Footer>
                <header><i>Task 3</i></header>
                <Section.Footer>
                    Сфотографироваться с 6 незнакомыми людьми
                </Section.Footer>
            </List>
        </div>

    )
}