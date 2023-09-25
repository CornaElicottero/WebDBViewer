import React, {useRef, useState} from 'react';
import {SearchBar, NavBar, ListItem, Form, Test} from "./components/index";
import {BrowserRouter, Route, Routes, useParams} from 'react-router-dom'
const App = () => {
    const [searchPayload, setSearchPayload] = useState("");
    const handleChangeSearchPayload = (value) => {
        setSearchPayload(value)
    }
    return (
    <div className="App">
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<>
                    <SearchBar onChangeSearchPayload={handleChangeSearchPayload} />
                    <ListItem searchPayload={searchPayload} />
                    <NavBar />
                </>} />
                <Route path="/new" element={<>
                    <Test />
                    <Form />

                </>} />
                <Route path="/edit" element={<>
                    <Form />
                </>} />
            </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
