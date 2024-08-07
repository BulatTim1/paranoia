import "./layout.css"

// @ts-ignore
export const Layout = ({children}) => {
    return(
        <div className="layout">
            <div>{children}</div>
        </div>
    )
}
