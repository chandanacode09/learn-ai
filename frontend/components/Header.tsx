export function Header() {
  return (
    <header className="border-b bg-white shadow-sm">
      <div className="container mx-auto px-4 py-4 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <span className="text-2xl">🧠</span>
          <span className="font-bold text-xl">AI Content Explainer</span>
        </div>

        <nav className="flex items-center gap-6">
          <a
            href="#"
            className="text-gray-600 hover:text-gray-900 transition-colors"
          >
            Features
          </a>
          <a
            href="#"
            className="text-gray-600 hover:text-gray-900 transition-colors"
          >
            Pricing
          </a>
          <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors">
            Get Started
          </button>
        </nav>
      </div>
    </header>
  );
}
