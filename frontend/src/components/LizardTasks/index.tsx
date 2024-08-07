import {List, Section} from "@telegram-apps/telegram-ui";

import "./index.css"
import {useEffect, useState} from "react";


export const LizardTasks = () => {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        fetch('/api/tasks')
            .then(response => response.json())
            .then(data => setTasks(data))
            .catch(error => console.error('Error fetching tasks:', error));
    }, []);

    return (
        <div>
            <List>
                {tasks.map(task => (
                    <Section key={task.id}>
                        <div>{task.description}</div>
                    </Section>
                ))}
            </List>
        </div>
    );
}