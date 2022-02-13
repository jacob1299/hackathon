import React from 'react'
import { Stack, Button } from '@chakra-ui/react'
import { useAuth0 } from "@auth0/auth0-react";
import { useNavigate } from 'react-router-dom'

interface LoginButtonProps {
  mr: number
}

export const LoginButton = ({mr}: LoginButtonProps) => {
  const { loginWithRedirect, isLoading, isAuthenticated } = useAuth0()
  let navigate = useNavigate()

  const login = () => {
    isAuthenticated && navigate('/main')
  }

  return (
    <Stack direction='row' spacing={4} align='center'>
        {!isAuthenticated && 
        <Button
          isLoading={isLoading}
          loadingText='Loading'
          colorScheme='black'
          variant='outline'
          spinnerPlacement='start'
          onClick={loginWithRedirect}
          mr={mr}
        >
          Log In 
        </Button>}
        {isAuthenticated && 
        <Button
          isLoading={isLoading}
          loadingText='Loading'
          colorScheme='black'
          variant='outline'
          spinnerPlacement='start'
          onClick={login}
          mr={mr}
        >
          Play Chess!
        </Button>}
    </Stack>
  ) 
}