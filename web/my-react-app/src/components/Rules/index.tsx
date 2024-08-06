import React from "react";
import {Cell, Section} from "@telegram-apps/telegram-ui";

import "./index.css"
import {
    SectionFooter
} from "@telegram-apps/telegram-ui/dist/components/Blocks/Section/components/SectionFooter/SectionFooter";


export const Rules = () => {

    // @ts-ignore
    return (
        <div>
            <a href="/" className="BackButton">Назад</a>
            <list>
                <Section>
                    <iframe src="https://www.youtube.com/embed/WFC4wxaZ5Qc"></iframe>
                </Section>

                <Cell
                    subtitle="Рекомендуется к просмотру">
                    <i>Правила игры</i>
                </Cell>
                <Section>
                    <SectionFooter>
                        <header>
                            Описание
                        </header>
                        <div className="RulesText">
                            В начале раунда игроки случайным образом делятся на Ящеров и Русов. Ящерам даются задания,
                            которые необходимо выполнить до 23:00. Их надо сделать в людных местах: зимний сад, зона
                            кофе-брейка, лекционный зал, столовая. У Русов есть 3 попытки написать в бот свои
                            подозрения. В
                            конце дня подводятся итоги и начисляются баллы.
                        </div>
                    </SectionFooter>
                </Section>
            </list>
        </div>
    )
}