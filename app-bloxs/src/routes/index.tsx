import  { UserContext }  from '../contexts/user';
import React, { useState } from 'react';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import SignUp from '../pages/sign-up/index';
import SignIn from '../pages/sign-in/index';
import Home from '../pages/home/index';
import Transactions from '../pages/transactions';
import Profile from '../pages/profile';

export const AppRoutes = ()=>{
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [token, setToken] = useState('');
    const [name, setName] = useState('');
    const [cpf, setCpf] = useState('');
    const [birth, setBirth] = useState('');

    return(
        <Router>
            <UserContext.Provider value={{email, setEmail, password, setPassword, token, 
                setToken, name, setName, cpf, setCpf, birth, setBirth}}>
                    <Routes>
                        <Route path='/signup' element={<SignUp />}/>
                        <Route path='/' element={<SignIn />}/>
                        <Route path='/home' element={<Home />}/>
                        <Route path='/transactions' element={<Transactions />}/>
                        <Route path='/profile' element={<Profile />}/>
                    </Routes>
            </UserContext.Provider>
        </Router>
    );
}