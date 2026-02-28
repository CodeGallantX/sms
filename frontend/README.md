# SchoolOS Platform Frontend

Enterprise-grade, multi-tenant white-label SaaS frontend for School Management.

## Tech Stack
- **Next.js 15 (App Router)**
- **TypeScript**
- **TailwindCSS**
- **Framer Motion** (Animations)
- **Zustand** (State Management)
- **React Query** (Data Fetching)
- **Axios** (API Interceptors)

## Core Features
- **Multi-Tenant Routing**: Subdomain-based tenant detection in `axios.ts` and `middleware.ts`.
- **Dynamic Theming**: CSS variable-based white-labeling via `ThemeProvider`.
- **Role-Based Access**: Route protection and dynamic layouts for Admin, Teacher, Student, etc.
- **Onboarding Wizard**: Multi-step institution configuration.
- **AI Integration Ready**: UI hooks for OpenAI-powered features.

## Getting Started
1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Set environment variables in `.env.local`:
   ```bash
   NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
   ```
4. Run development server: `npm run dev`

## Directory Structure
- `app/`: App Router pages and layouts.
- `components/`: Reusable UI components.
- `lib/axios.ts`: API client with tenant headers.
- `store/`: Global state (Auth, Tenant).
- `themes/`: White-label theme provider.
