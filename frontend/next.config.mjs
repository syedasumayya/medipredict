// frontend/next.config.mjs
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Allow the Next.js server to proxy API requests to the backend during production
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://localhost:8000/:path*',
      },
    ];
  },
};

export default nextConfig;