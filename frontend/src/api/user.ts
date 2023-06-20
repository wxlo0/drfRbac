import http from '@/utils/http'

export async function userLogin(data) {
    return await http.post('/user/login', data)
}

