import React from "react";
import "./layout.css"

export const Layout = ({children}) => {
    return(
        <div className="layout">
            <div>{children}</div>
        </div>
    )
}
