import { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { UserContext } from '../../contexts/user';

import { Header, MenuItem, Page, Logo } from '../../styles/common-structure';
import { TransactionsCard, TitlePage, Line, TransactionsContainer } from './style';

import Transaction from '../../components/Transaction';

import LogoTotal from '../../assets/icon/logotype-infinity-bank.svg';

const Transactions = () => {
    const { setToken } = useContext(UserContext);

    let transactionMocked = {' is_sender': true, 'value': 100, 'date': '2023-02-10T00:00:00' }
    let navigate = useNavigate();

    const Logout = () => {
        sessionStorage.removeItem('token');   
        setToken('');
        navigate('/signin');
    }

    const GoToHome = () => {
        navigate('/home');
    }

    return (
        <Page>
            <Header>
                <Logo src={LogoTotal} onClick={GoToHome}/>
                <MenuItem onClick={Logout}>
                    Sair
                </MenuItem>
                <MenuItem>
                    Sobre
                </MenuItem>
                <MenuItem>
                    Transações
                </MenuItem>
            </Header>
            <TitlePage>Transações Bancárias</TitlePage>
            <Line>
                <TransactionsCard>
                    <TransactionsContainer>
                        <Transaction transaction={transactionMocked}></Transaction>
                        <Transaction transaction={transactionMocked}></Transaction>
                        <Transaction transaction={transactionMocked}></Transaction>
                        <Transaction transaction={transactionMocked}></Transaction>
                        <Transaction transaction={transactionMocked}></Transaction>
                        <Transaction transaction={transactionMocked}></Transaction>
                    </TransactionsContainer>
                </TransactionsCard>
            </Line>
            
        </Page>
    )
}

export default Transactions;