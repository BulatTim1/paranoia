import React from "react";
import {useNavigate, useSearchParams} from "react-router-dom";
import {instruction} from "../menu_routes.ts";
import {Button} from "@telegram-apps/telegram-ui";

export const About = () => {
    const navigate = useNavigate()

    const [searchParams] = useSearchParams();
    const id = searchParams.get("id");
    const elem = instruction[id];

    return (<div>
            <div>Name: {elem.name}</div>
            <div>Status: {elem.status}</div>
            <div>Time: {new Date(elem.time).toDateString()}</div>
            <div>
                <Button
                    onClick={() => navigate("/")}
                    mode="filled"
                    size="s"
                >
                    Back</Button>
            </div>
        </div>
    )
}