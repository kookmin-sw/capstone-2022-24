import oauth from '@/mocks/handlers/oauth';
import register from '@/mocks/handlers/register';

export const handlers = [...Object.values(oauth), ...Object.values(register)];
