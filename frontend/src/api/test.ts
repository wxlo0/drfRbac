import http from '@/utils/http'

export async function TestApi() {
    return await http.get('/course/classification')
}

