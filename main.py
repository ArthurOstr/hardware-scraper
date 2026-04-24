from core.network import NetworkFetcher
from parsers.telemart import TelemartParser


def test_target():
    fetcher = NetworkFetcher()

    target_url = "https://telemart.ua/ua/processor/"
    print("Initializing network test...")
    raw_html = fetcher.fetch_page(target_url)

    if raw_html:
        parser = TelemartParser(raw_html)
        extracted_cpus = parser.extract_items()

        print(f"\n[+] Success. Extracted {len(extracted_cpus)} Component models.")

        if extracted_cpus:
            print("\n--- Sample Output ---")
            print(extracted_cpus[0].model_dump_json(indent=2))
            print("------------------\n")
        else:
            print("\n[-] Extraction failed.")

    fetcher.close()


if __name__ == "__main__":
    test_target()
