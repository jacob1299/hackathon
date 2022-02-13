import React, { useEffect } from 'react'
import { Stack, Button } from '@chakra-ui/react'
import { useAuth0 } from "@auth0/auth0-react";
import { useNavigate } from 'react-router-dom'


interface LoginButtonProps {
  mr?: number
}

export const LoginButton = ({mr}: LoginButtonProps) => {
  const { loginWithRedirect, isAuthenticated, isLoading } = useAuth0()
  let navigate = useNavigate()

  useEffect(() => {
    isAuthenticated && navigate('/main')
  }, [navigate, isAuthenticated])

  return (
    <Stack direction='row' spacing={4} align='center'>
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
        </Button> 
    </Stack>
  ) 
}