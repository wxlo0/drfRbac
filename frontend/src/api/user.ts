import http from '@/utils/http'

export async function userLogin(data) {
    return await http.post('/user/login', data)
}

export async function userList() {
    return await http.get('/user/list')
}

export async function roleList() {
    return await http.get('/user/role/list')
}

export async function roleChange(userId, data) {
    return await http.put(`/user/role/change/${userId}`, data)
}

