import { Avatar } from "@telegram-apps/telegram-ui"

export const instruction = [
    {
        index: 0,
        name: "Game rules",
        text: "Правила игры",
        description: "",
        path: "/rules",
        image: "https://github.com/goforbg/telegram-emoji-gifs/blob/master/nerd.gif?raw=true"
    },
    {
        index: 1,
        name: "Player types",
        text: "Типы игроков",
        description: "",
        path: "/PlayerTypes",
        image: "https://github.com/goforbg/telegram-emoji-gifs/blob/master/0-moon.gif?raw=true"
    }
]
export const game_menu = [
    {
        index: 0,
        name: "Suspects",
        text: "Ввод подозреваемых",
        description: "3 попытки в раунд",
        path: "/sus-input",
        image: "https://github.com/goforbg/telegram-emoji-gifs/blob/master/0-moon.gif"
    }, {
        index: 1,
        name: "Lizard tasks",
        text: "Задания для Ящеров",
        description: "список задач",
        path: "/lizard-tasks",
        image: "https://github.com/goforbg/telegram-emoji-gifs/blob/master/0-moon.gif"
    }, {
        index: 2,
        name: "Game results",
        text: "Подведение итогов",
        description: "голосование",
        path: "/result",
        image: "https://github.com/goforbg/telegram-emoji-gifs/blob/master/0-moon.gif"
    }, {
        index: 3,
        name: "Overall rating",
        text: "Общий рейтинг",
        description: "баллы",
        path: "/rating",
        image: "https://github.com/goforbg/telegram-emoji-gifs/blob/master/0-moon.gif"
    },
]