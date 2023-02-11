import { TitlePage, Page, Header, Logo, 
        MenuItem, Line } from '../../styles/common-structure';

import { ActionButton } from '../../styles/main-auth-structure';

import { Text, TextContainer, ChangeAccountStatus } from './styles';
import LogoTotal from '../../assets/icon/logotype-infinity-bank.svg';
import { UserContext } from '../../contexts/user';
import { useContext, useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { Get, BlockAccount } from '../../services/crud';
const Profile = () => {

    const { setToken } = useContext(UserContext);
    const [account, setAccount] = useState({'name': '', 'amount': '', 'email': '', 'cpf': ''});

    let navigate = useNavigate();

    const Logout = () => {
        sessionStorage.removeItem('token');   
        setToken('');
        navigate('/');
    }
    
    const goToTransactions = () => {
        navigate('/transactions')
    }

    const Block = () => {
        let token = sessionStorage.getItem('token') || '';
        BlockAccount(token, [])
    }

    const GoToHome = () => {
        navigate('/home');
    }

    useEffect(() => {
        const GetAccountInfo = async () => {
            let token = sessionStorage.getItem('token') || '';
            await Get('account', token, setAccount);
            
        }

        GetAccountInfo();
    }, [])

    return (
        <Page>
            <Header>
                <Logo src={LogoTotal} onClick={GoToHome}/>
                <MenuItem onClick={Logout}>
                    Sair
                </MenuItem>
                <MenuItem>
                    Meu Perfil
                </MenuItem>
                <MenuItem onClick={goToTransactions}>
                    Transações
                </MenuItem>
            </Header>
            <TitlePage>Meu Perfil</TitlePage>
            <TextContainer>
                <Text>{ account.name }</Text>
                <Text>{ account.email }</Text>
                <Text>{ account.cpf }</Text>
            </TextContainer>
            <ChangeAccountStatus onClick={Block}>Bloquear Conta</ChangeAccountStatus>
        </Page>
    )
}

export default Profile;