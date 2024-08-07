import {List, Section} from "@telegram-apps/telegram-ui";

import "./index.css"
import {useEffect, useState} from "react";
import axios from "axios";

export const LizardTasks = () => {

    return (
        <div>
            <h1 className="text-center">List of Books</h1>
            <br />
            <Row xs={1} md={2} className="g-4">
                {books &&
                    books.map((book, id) => (
                        <Col key={id}>

                            <Card key={id}>

                                <Card.Body>
                                    <Card.Title>{book.title}</Card.Title>
                                    <Card.Text>{book.description}</Card.Text>
                                </Card.Body>
                            </Card>
                        </Col>
                    ))}
            </Row>
        </div>
    );
};