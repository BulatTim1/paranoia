import { Cell, Image, List, Section } from "@telegram-apps/telegram-ui";


export const Leaderboard = () => {

    return (
        <List>
            <a href="/" className="BackButton">Назад</a>

            <Section
                header="Результаты"
            >
                <Cell before={<Image size={48} src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Telegram-Animated-Emojis/main/Activity/1st%20Place%20Medal.webp"></Image>}>
                    Иванов Иван Иванович
                </Cell>
                <Cell before={<Image size={48} src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Telegram-Animated-Emojis/main/Activity/2nd%20Place%20Medal.webp"></Image>}>
                    Сергеев Сергей Сергеевич
                </Cell>
                <Cell before={<Image size={48} src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Telegram-Animated-Emojis/main/Activity/3rd%20Place%20Medal.webp"></Image>}>
                    Смирнов Максим Андреевич
                </Cell>
            </Section>
        </List>
    )
}