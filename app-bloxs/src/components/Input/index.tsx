import React,{useEffect, useState, useContext} from 'react'
import  { UserContext }  from '../../contexts/user';

import {Input, InputPasswordContainer, InputPassword, PasswordPreview, IncorrectEmailWarning} from './style';
import Eye from '../../assets/icon/eye.svg';
import EyeSlash from '../../assets/icon/eye-slash.svg';

const InputComponent = (props:any)=>{
    
    let inputType:string = props.inputType;
    const { setEmail, password, setPassword, setName, name, cpf, setCpf, setBirth } = useContext(UserContext);

    const [passwordIsVisible, setPasswordIsVisible] = useState(true);
    const [passwordTypeView, setPasswordTypeView] = useState('password');
    const [emailContent, setEmailContent] = useState('');
    const [birthContent, setBirthContent] = useState('');
    const [testValidation, setTestValidation] = useState(null);
    
    const ChangeSecureText=()=>{
        setPasswordIsVisible(!passwordIsVisible);
    }

    const DateValidation = (event: React.ChangeEvent<HTMLInputElement>)=>{
        setBirthContent(event.target.value);
        setBirth(event.target.value)
    }

    const EmailValidation = (event: React.ChangeEvent<HTMLInputElement>)=>{
        let emailRegex:any =  /\S+@\S+\.\S+/;
        setEmailContent(event.target.value);
        setEmail(event.target.value);
        setTestValidation(emailRegex.test(emailContent));
    }

    const PasswordValidation = (event: React.ChangeEvent<HTMLInputElement>)=>{
        setPassword(event.target.value);
    }

    const NameValidation = (event: React.ChangeEvent<HTMLInputElement>)=>{
        setName(event.target.value);
        
    }

    const CpfValidation = (event: React.ChangeEvent<HTMLInputElement>)=>{
        setCpf(event.target.value);
    }

    useEffect(()=>{
        
        if (passwordIsVisible === true){
            setPasswordTypeView('password');
        }
        else{
            setPasswordTypeView('text');
        }
    })
    return(
        <>
            {
                inputType === 'password' ?
                    <InputPasswordContainer style={password.length > 6? {borderColor: '#2ecc71'} : {borderColor: '#6A6A6A'}}>
                        <InputPassword placeholder={inputType} onChange={PasswordValidation} required type={passwordTypeView}/>
                        <PasswordPreview type='button' onClick={ChangeSecureText}>
                            { passwordIsVisible ? <img src={Eye} width={22} height={16} alt="view password" draggable={false}/> : <img src={EyeSlash} width={25} height={20} alt="view password" draggable={false}/> }
                        </PasswordPreview>
                    </InputPasswordContainer>
                :
                inputType === 'email' ?
                    <>
                        <Input placeholder={inputType} onChange={EmailValidation} validation={testValidation} required/>
                        {
                            testValidation === false ?
                            <IncorrectEmailWarning>Your email should look like this: username@server.com!</IncorrectEmailWarning>
                            :
                            <></>
                        }
                    </>
                : 
                inputType === 'name'?
                <>
                    <Input placeholder={inputType} onChange={NameValidation} validation={name.length > 6? true : undefined} required/>
                </>
                :
                inputType === 'cpf'?
                <>
                    <Input placeholder={inputType} onChange={CpfValidation} validation={cpf.length == 11? true : undefined} required/>
                </>
                :
                inputType === 'date'?
                <>
                    <Input type={inputType} placeholder={'21/06/1998'} onChange={DateValidation} validation={birthContent !== ''? true : undefined} required/>
                </>
                :
                <></>
            }
        </>
    );
}

export default InputComponent;