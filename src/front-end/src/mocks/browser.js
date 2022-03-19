import { setupWorker } from 'msw';
import { handlers } from '@/mocks/handlers/index.js';

export const worker = setupWorker(...handlers);
