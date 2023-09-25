import React from 'react';
import {Link} from "react-router-dom";

const NavBar = () => {
    return (
        <div className={"btn_wrapper"}>
            <div className={"nav_btn"}>
                <button className={"btn"}>&lt;</button>
                <button className={"btn"}>&gt;</button>
            </div>
            <div className={"edit_btn"}>
                <Link to="/new">
                    <button className={"btn"}>Новая</button>
                </Link>
                <Link to="/edit">
                    <button className={"btn"}>Редактировать</button>
                </Link>
                <button className={"btn"}>Отчёт</button>
            </div>
        </div>
    );
};

export default NavBar;
